# agents/data_reader.py
import pandas as pd
import sqlite3
import requests
from typing import Dict, Any


class DataReaderAgent:
    """
    This agent is like a smart librarian - it knows how to read different types of books (data sources)
    """

    def __init__(self):
        self.supported_formats = ['csv', 'excel', 'json', 'sql', 'api']

    def read_csv(self, file_path: str) -> pd.DataFrame:
        """Read CSV file - like reading a simple table"""
        try:
            data = pd.read_csv(file_path)
            print(f"✅ Successfully read CSV with {len(data)} rows")
            return data
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return pd.DataFrame()

    def read_excel(self, file_path: str, sheet_name: str = None) -> pd.DataFrame:
        """Read Excel file - like reading a spreadsheet"""
        try:
            data = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"✅ Successfully read Excel with {len(data)} rows")
            return data
        except Exception as e:
            print(f"❌ Error reading Excel: {e}")
            return pd.DataFrame()

    def read_database(self, db_path: str, query: str) -> pd.DataFrame:
        """Read from database - like asking a filing cabinet for specific files"""
        try:
            conn = sqlite3.connect(db_path)
            data = pd.read_sql_query(query, conn)
            conn.close()
            print(f"✅ Successfully read database with {len(data)} rows")
            return data
        except Exception as e:
            print(f"❌ Error reading database: {e}")
            return pd.DataFrame()

    def read_api(self, url: str, params: Dict = None) -> pd.DataFrame:
        """Read from API - like calling someone and asking for information"""
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = pd.DataFrame(response.json())
                print(f"✅ Successfully read API data with {len(data)} rows")
                return data
            else:
                print(f"❌ API request failed with status {response.status_code}")
                return pd.DataFrame()
        except Exception as e:
            print(f"❌ Error reading API: {e}")
            return pd.DataFrame()

    def get_data_info(self, data: pd.DataFrame) -> Dict[str, Any]:
        """Get information about the data - like getting a summary of a book"""
        if data.empty:
            return {"error": "No data available"}

        info = {
            "rows": len(data),
            "columns": len(data.columns),
            "column_names": data.columns.tolist(),
            "data_types": data.dtypes.to_dict(),
            "missing_values": data.isnull().sum().to_dict(),
            "sample_data": data.head().to_dict()
        }
        return info