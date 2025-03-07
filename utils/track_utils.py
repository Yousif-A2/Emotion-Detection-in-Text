import os
import pytz
from datetime import datetime
import psycopg2
from psycopg2 import pool
import streamlit as st

# Define timezone
IST = pytz.timezone('Asia/Kolkata')

# Create a connection pool
@st.cache_resource
def init_connection_pool():
    return psycopg2.pool.SimpleConnectionPool(1, 10,
        host=st.secrets["db_host"],
        database=st.secrets["db_name"],
        user=st.secrets["db_user"],
        password=st.secrets["db_password"],
        port=st.secrets["db_port"],
        sslmode=st.secrets["db_sslmode"]

    )

# Get a connection from the pool
def get_conn():
    try:
        return init_connection_pool().getconn()
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Release the connection back to the pool
def release_conn(conn):
    init_connection_pool().putconn(conn)

# Execute a query and commit changes
def execute_query(query, params=None, fetch=False):
    conn = get_conn()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query, params or ())
                if fetch:
                    result = cur.fetchall()
                else:
                    result = None
                conn.commit()
                return result
        except Exception as e:
            conn.rollback()
            st.error(f"Database error: {e}")
            return None
        finally:
            release_conn(conn)
    return None

# Function to create page visited table
def create_page_visited_table():
    query = '''
    CREATE TABLE IF NOT EXISTS page_track_table (
        id SERIAL PRIMARY KEY,
        pagename TEXT NOT NULL,
        time_of_visit TIMESTAMP WITH TIME ZONE NOT NULL
    )
    '''
    execute_query(query)

# Function to add page visited details
def add_page_visited_details(pagename, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST)
    query = 'INSERT INTO page_track_table(pagename, time_of_visit) VALUES (%s, %s)'
    execute_query(query, (pagename, timeOfvisit))

# Function to view all page visited details
def view_all_page_visited_details():
    query = 'SELECT pagename, time_of_visit FROM page_track_table ORDER BY time_of_visit DESC'
    results = execute_query(query, fetch=True)
    return results or []

# Function to create emotion classifier table
def create_emotionclf_table():
    query = '''
    CREATE TABLE IF NOT EXISTS emotionclf_table (
        id SERIAL PRIMARY KEY,
        rawtext TEXT NOT NULL,
        prediction TEXT NOT NULL,
        probability NUMERIC NOT NULL,
        time_of_visit TIMESTAMP WITH TIME ZONE NOT NULL
    )
    '''
    execute_query(query)

# Function to add prediction details
def add_prediction_details(rawtext, prediction, probability, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST)
    query = 'INSERT INTO emotionclf_table(rawtext, prediction, probability, time_of_visit) VALUES (%s, %s, %s, %s)'
    execute_query(query, (rawtext, prediction, probability, timeOfvisit))

# Function to view all prediction details
def view_all_prediction_details():
    query = 'SELECT rawtext, prediction, probability, time_of_visit FROM emotionclf_table ORDER BY time_of_visit DESC'
    results = execute_query(query, fetch=True)
    return results or []