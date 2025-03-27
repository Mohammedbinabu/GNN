import sqlite3
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv # For Graph Convolutional Networks
from functools import lru_cache
from sentence_transformers import SentenceTransformer # For prompt embeddings
from torch.utils.data import DataLoader, TensorDataset

class DatabaseManager:
    def __init__(self, db_path="employee_management0.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            print("Database connection successful!")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close_db(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Example usage
db_manager = DatabaseManager()