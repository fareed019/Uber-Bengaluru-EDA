"""
Uber Bengaluru Case Study - EDA Analysis Script
================================================

This script performs comprehensive exploratory data analysis on Uber ride data
from Bengaluru (Bangalore), India.

Author: [Your Name]
Date: 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configuration
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# 1. DATA LOADING & INITIAL EXPLORATION
# ============================================================================

def load_data(filepath):
    """Load and display basic information about the dataset."""
    print("\n" + "="*80)
    print("DATA LOADING & EXPLORATION")
    print("="*80)
    
    df = pd.read_csv(filepath)
    
    print(f"\n📊 Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\n📋 First few records:")
    print(df.head())
    
    print(f"\n📈 Data Info:")
    print(df.info())
    
    print(f"\n📉 Descriptive Statistics:")
    print(df.describe())
    
    return df


# ============================================================================
# 2. DATA CLEANING & PREPROCESSING
# ============================================================================

def preprocess_data(df):
    """Clean and preprocess the dataset."""
    print("\n" + "="*80)
    print("DATA CLEANING & PREPROCESSING")
    print("="*80)
    
    df_clean = df.copy()
    
    # Convert timestamp columns to datetime
    if 'Request timestamp' in df_clean.columns:
        df_clean['Request timestamp'] = pd.to_datetime(df_clean['Request timestamp'])
    
    if 'Drop timestamp' in df_clean.columns:
        df_clean['Drop timestamp'] = pd.to_datetime(df_clean['Drop timestamp'])
    
    # Feature Engineering: Extract hour from timestamp
    if 'Request timestamp' in df_clean.columns:
        df_clean['RequestHour'] = df_clean['Request timestamp'].dt.hour
    
    # Feature Engineering: Create time slots
    def assign_timeslot(hour):
        """Assign time period based on hour of day."""
        if hour <= 4:
            return 'Dawn'
        elif hour <= 8:
            return 'Morning'
        elif hour <= 12:
            return 'Midday'
        elif hour <= 16:
            return 'Afternoon'
        elif hour <= 20:
            return 'Evening'
        else:
            return 'Night'
    
    if 'RequestHour' in df_clean.columns:
        df_clean['TimeSlot'] = df_clean['RequestHour'].apply(assign_timeslot)
    
    # Feature Engineering: Cab Availability
    def cab_availability(status):
        """Determine if cab was available."""
        return 'Available' if status == 'Trip Completed' else 'Not Available'
    
    if 'Status' in df_clean.columns:
        df_clean['Cab Availability'] = df_clean['Status'].apply(cab_availability)
    
    print(f"✅ Data cleaned successfully!")
    print(f"   - Timestamps converted to datetime format")
    print(f"   - Time features extracted (Hour, TimeSlot)")
    print(f"   - Cab availability feature created")
    
    return df_clean


# ============================================================================
# 3. DESCRIPTIVE STATISTICS
# ============================================================================

def analyze_status(df):
    """Analyze request status distribution."""
    print("\n" + "="*80)
    print("REQUEST STATUS ANALYSIS")
    print("="*80)
    
    status_counts = df['Status'].value_counts()
    status_pct = df['Status'].value_counts(normalize=True) * 100
    
    print("\n📊 Request Status Distribution:")
    for status in status_counts.index:
        print(f"   {status:20s}: {status_counts[status]:6d} ({status_pct[status]:5.2f}%)")
    
    print(f"\n💡 Key Insight: The most common status indicates system behavior patterns.")
    
    return status_counts


def analyze_pickup_locations(df):
    """Analyze demand by pickup location."""
    print("\n" + "="*80)
    print("PICKUP LOCATION ANALYSIS")
    print("="*80)
    
    if 'Pickup point' in df.columns:
        location_counts = df['Pickup point'].value_counts()
        location_pct = df['Pickup point'].value_counts(normalize=True) * 100
        
        print("\n📍 Requests by Pickup Location:")
        for location in location_counts.index:
            print(f"   {location:15s}: {location_counts[location]:6d} ({location_pct[location]:5.2f}%)")
        
        return location_counts
    else:
        print("   ⚠️  Pickup point column not found")
        return None


def analyze_hourly_demand(df):
    """Analyze demand patterns by hour of day."""
    print("\n" + "="*80)
    print("HOURLY DEMAND ANALYSIS")
    print("="*80)
    
    if 'RequestHour' in df.columns:
        hourly_demand = df.groupby('RequestHour').size()
        
        print("\n⏰ Requests by Hour of Day:")
        print(f"   Peak Hour: {hourly_demand.idxmax()}:00 with {hourly_demand.max()} requests")
        print(f"   Off-Peak Hour: {hourly_demand.idxmin()}:00 with {hourly_demand.min()} requests")
        print(f"   Average Requests/Hour: {hourly_demand.mean():.2f}")
        
        print("\n📊 Hourly Breakdown:")
        for hour in range(24):
            if hour in hourly_demand.index:
                print(f"   {hour:02d}:00 - {hour+1:02d}:00: {hourly_demand[hour]:6d} requests")
        
        return hourly_demand
    else:
        print("   ⚠️  RequestHour column not found")
        return None


def analyze_by_location_and_status(df):
    """Analyze status distribution by pickup location."""
    print("\n" + "="*80)
    print("STATUS ANALYSIS BY LOCATION")
    print("="*80)
    
    if 'Pickup point' in df.columns and 'Status' in df.columns:
        location_status = pd.crosstab(df['Pickup point'], df['Status'])
        
        print("\n📊 Request Status by Pickup Location:")
        print(location_status)
        
        print("\n💡 Percentage Distribution by Location:")
        location_status_pct = pd.crosstab(df['Pickup point'], df['Status'], normalize='index') * 100
        print(location_status_pct.round(2))
        
        return location_status
    else:
        print("   ⚠️  Required columns not found")
        return None


# ============================================================================
# 4. VISUALIZATIONS
# ============================================================================

def create_visualizations(df, output_dir='./images/'):
    """Generate all visualizations."""
    print("\n" + "="*80)
    print("GENERATING VISUALIZATIONS")
    print("="*80)
    
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Status Distribution Bar Chart
    if 'Status' in df.columns:
        plt.figure(figsize=(10, 6))
        status_counts = df['Status'].value_counts()
        plt.bar(status_counts.index, status_counts.values, color=['#06C167', '#FF6B6B', '#FFD93D'])
        plt.title('Request Status Distribution', fontsize=16, fontweight='bold')
        plt.xlabel('Status', fontsize=12)
        plt.ylabel('Number of Requests', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}01_status_distribution.png', dpi=300, bbox_inches='tight')
        print("✅ Saved: 01_status_distribution.png")
        plt.close()
    
    # 2. Hourly Demand Line Chart
    if 'RequestHour' in df.columns:
        plt.figure(figsize=(12, 6))
        hourly_demand = df.groupby('RequestHour').size()
        plt.plot(hourly_demand.index, hourly_demand.values, marker='o', linewidth=2, markersize=8, color='#06C167')
        plt.fill_between(hourly_demand.index, hourly_demand.values, alpha=0.3, color='#06C167')
        plt.title('Hourly Demand Pattern', fontsize=16, fontweight='bold')
        plt.xlabel('Hour of Day', fontsize=12)
        plt.ylabel('Number of Requests', fontsize=12)
        plt.xticks(range(0, 24, 2))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}02_hourly_demand.png', dpi=300, bbox_inches='tight')
        print("✅ Saved: 02_hourly_demand.png")
        plt.close()
    
    # 3. Pickup Location Comparison
    if 'Pickup point' in df.columns:
        plt.figure(figsize=(10, 6))
        location_counts = df['Pickup point'].value_counts()
        colors = ['#06C167', '#FF6B6B']
        plt.bar(location_counts.index, location_counts.values, color=colors)
        plt.title('Requests by Pickup Location', fontsize=16, fontweight='bold')
        plt.xlabel('Pickup Location', fontsize=12)
        plt.ylabel('Number of Requests', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}03_pickup_location_comparison.png', dpi=300, bbox_inches='tight')
        print("✅ Saved: 03_pickup_location_comparison.png")
        plt.close()
    
    # 4. Status by Hour (Stacked Bar)
    if 'RequestHour' in df.columns and 'Status' in df.columns:
        plt.figure(figsize=(14, 6))
        hourly_status = df.groupby(['RequestHour', 'Status']).size().unstack(fill_value=0)
        hourly_status.plot(kind='bar', stacked=False, ax=plt.gca(), colormap='viridis')
        plt.title('Request Status by Hour of Day', fontsize=16, fontweight='bold')
        plt.xlabel('Hour of Day', fontsize=12)
        plt.ylabel('Number of Requests', fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{output_dir}04_status_by_hour.png', dpi=300, bbox_inches='tight')
        print("✅ Saved: 04_status_by_hour.png")
        plt.close()
    
    # 5. City Pickup Analysis
    if 'Pickup point' in df.columns and 'RequestHour' in df.columns:
        df_city = df[df['Pickup point'] == 'City']
        if len(df_city) > 0:
            plt.figure(figsize=(12, 6))
            city_hourly = df_city.groupby('RequestHour').size()
            plt.bar(city_hourly.index, city_hourly.values, color='#06C167', alpha=0.8)
            plt.title('Hourly Demand - City Pickup', fontsize=16, fontweight='bold')
            plt.xlabel('Hour of Day', fontsize=12)
            plt.ylabel('Number of Requests', fontsize=12)
            plt.xticks(range(0, 24, 2))
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.savefig(f'{output_dir}05_city_pickup_analysis.png', dpi=300, bbox_inches='tight')
            print("✅ Saved: 05_city_pickup_analysis.png")
            plt.close()
    
    # 6. Airport Pickup Analysis
    if 'Pickup point' in df.columns and 'RequestHour' in df.columns:
        df_airport = df[df['Pickup point'] == 'Airport']
        if len(df_airport) > 0:
            plt.figure(figsize=(12, 6))
            airport_hourly = df_airport.groupby('RequestHour').size()
            plt.bar(airport_hourly.index, airport_hourly.values, color='#FF6B6B', alpha=0.8)
            plt.title('Hourly Demand - Airport Pickup', fontsize=16, fontweight='bold')
            plt.xlabel('Hour of Day', fontsize=12)
            plt.ylabel('Number of Requests', fontsize=12)
            plt.xticks(range(0, 24, 2))
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.savefig(f'{output_dir}06_airport_pickup_analysis.png', dpi=300, bbox_inches='tight')
            print("✅ Saved: 06_airport_pickup_analysis.png")
            plt.close()
    
    print(f"\n✨ All visualizations saved to '{output_dir}' directory!")


# ============================================================================
# 5. MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "🚗 UBER BENGALURU EDA - ANALYSIS REPORT" + " "*18 + "║")
    print("╚" + "="*78 + "╝")
    
    # Change this to your actual data file path
    data_path = './data/uber-data.csv'
    
    try:
        # Load data
        df = load_data(data_path)
        
        # Preprocess data
        df_clean = preprocess_data(df)
        
        # Analyze status
        analyze_status(df_clean)
        
        # Analyze locations
        analyze_pickup_locations(df_clean)
        
        # Analyze hourly demand
        analyze_hourly_demand(df_clean)
        
        # Analyze by location and status
        analyze_by_location_and_status(df_clean)
        
        # Create visualizations
        create_visualizations(df_clean)
        
        print("\n" + "="*80)
        print("✅ ANALYSIS COMPLETE!")
        print("="*80)
        print("\n📊 Summary:")
        print(f"   - Processed {len(df_clean)} ride requests")
        print(f"   - Generated 6 visualizations")
        print(f"   - Created feature engineering pipeline")
        print(f"   - Identified demand patterns and availability issues")
        
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at '{data_path}'")
        print("   Please ensure 'uber-data.csv' is in the './data/' directory")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
