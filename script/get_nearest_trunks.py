#!/usr/bin/python3

import logging
import argparse
import os
import csv

logger = logging.getLogger(__name__)

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "external", "Mobile_Food_Facility_Permit.csv")

def parse_arguments():
  '''
  Parse command line arguments
  '''
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--csv_path', help='Path to CSV file',
                      default=CSV_FILE_PATH)
  parser.add_argument('-o', '--log-level', help='Log level', default='INFO',
                      choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
  parser.add_argument('-n', '--number', help='Number of nearest trucks', default=5, type=int)
  parser.add_argument('-a', '--latitude', help='Latitude', type=float, required=True)
  parser.add_argument('-g', '--longitude', help='Longitude', type=float, required=True)

  args, _ = parser.parse_known_args()
  return args

def get_csv(csv_path):
  '''
  Get csv content
  '''
  with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    trucks = [ row for row in reader if row["FacilityType"] == "Truck" ]
    return trucks

def get_distance_square(truck, latitude, longitude):
  return ((float(truck["Latitude"]) - latitude)**2 + (float(truck["Longitude"]) - longitude)**2)

def get_nearest_trucks(trucks, latitude, longitude, num):
  '''
  Get nearest trucks
  '''
  truck_with_distances = [
    (get_distance_square(truck, latitude, longitude), truck) for truck in trucks
  ]
  sorted_truck_with_distances = sorted(truck_with_distances, key=lambda item: item[0])
  return [ item [1] for item in sorted_truck_with_distances[:num] ]

def print_trucks(trucks):
  '''
  Print trucks information
  '''
  for truck in trucks:
    print(f'{truck["Applicant"]}\t{truck["Address"]}')

def main():
  args = parse_arguments()
  logging.basicConfig(level=getattr(logging, args.log_level))

  try:
    # Load trucks in csv
    logger.debug(f"Load CSV file {args.csv_path}")
    csv_data = get_csv(args.csv_path)
    logger.debug(f"Get {len(csv_data)} trucks from CSV file {args.csv_path}")

    # Get nearest trucks
    logger.debug(f"Get nearest {args.number} trucks")
    nearest_trucks = get_nearest_trucks(csv_data, args.latitude, args.longitude, args.number)

    # Print information
    print_trucks(nearest_trucks)

  except Exception as e:
    logger.exception(f"Error: {e}")

if __name__ == "__main__":
  main()
