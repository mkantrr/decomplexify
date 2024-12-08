from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import sys
import argparse
from behave.__main__ import Configuration, run_behave
from importlib import reload
from pprint import pprint


from behave_runner import AgentBasedModelingRunner
import globals
from features.models import AgentBasedModel
from executive_main import setup_files, break_down

api = Flask(__name__)
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

# Function to create text files from data
def create_text_files(data):
    # Create a directory to store the files
    if not os.path.exists('features'):
        os.makedirs('features')

    # Iterate through each key-value pair and write to a text file
    for key, value in data.items():
        with open(os.path.join('features', f"{key}.feature"), 'w') as f:
            f.write(f"Feature: Make the {key}\n\n")
            f.write(f"Scenario: Creation of {key}\n\n")
            f.write(value)
            
def run_model_creation():
    try:
        # Add logging to trace the flow
        orig_stdout = sys.stdout
        f = open('behave.out', 'w')
        sys.stdout = f
        print("Starting Behave run...") 
        
        globals.init()
       
        setup_files() 
        config = Configuration(verbose=True)
        retval = run_behave(config, runner_class=AgentBasedModelingRunner)
        
        pprint(vars(globals.MODEL)) 
        pprint(vars(globals.runtime_context)) 
        if retval != 0:
            raise SystemError("Gherkin grammar rules could not run properly. Check your syntax!")
        
        sys.stdout = orig_stdout
        f.close()
        
    except Exception as e:
        print(f"Error during Gherkin grammar run: {e}")
        raise e
    
def get_single_agent_grid_data(model):
        """ Return grid data at current state of grid in 2D array format"""
        # Initialize an empty 2D array to store the grid data
        grid_data = []
        
        # Assuming globals.MODEL.grid is a MultiGrid, we iterate over the grid's cells
        for x in range(model.grid.width):
            row_data = []
            for y in range(model.grid.height):
                # Get the list of agents in the cell (we assume one agent per cell)
                agent = model.grid.get_cell_list_contents((x, y))
                if agent:
                    agent_classname = type(agent[0]).__name__
                    class_number = globals.agent_dict.get(agent_classname, None)
                    row_data.append(class_number)
                else:
                    row_data.append(None)  # Empty cell
            grid_data.append(row_data)
        return grid_data
    
# Health Check Route
@api.route('/api/healthcheck', methods=['GET'])
def health_check():
    """Health check endpoint to verify the app is running"""
    return jsonify({"status": "ok", "message": "Service is healthy"}), 200

# Endpoint to handle the creation of text files
@api.route('/api/create', methods=['POST'])
def create_files():
    data = request.json  # This will be None if no body is provided or body is incorrectly formatted
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    if len(data) != 5:
        return jsonify({'error': 'Request does not contain the correct amount of model definitions!'}), 400
    
    try:
        create_text_files(data)
        print("Feature files created successfully!")
        run_model_creation() 
        print("Behave ran successfully!")
        return jsonify({'message': 'Definitions created successfully!', 
                        'key': type(globals.MODEL.grid).__name__,
                        'grid': get_single_agent_grid_data(globals.MODEL)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
# Endpoint to handle the creation of text files
@api.route('/api/model-data', methods=['GET'])
def fetch_model_dataframe():
    try:
        print(f"Fetching model data: {globals.MODEL.datacollector.get_model_vars_dataframe()}")
        data = globals.MODEL.datacollector.get_model_vars_dataframe()
        return jsonify({"columns": data.columns.tolist(), "data": data.values.tolist()}), 200
    except Exception as e:
        print(f"Error fetching model data: {e}")
        return jsonify({'error': str(e)}), 500

# Endpoint to handle the creation of text files
@api.route('/api/agent-data', methods=['GET'])
def fetch_agent_dataframe():
    try:
        print(f"Fetching agent data: {globals.MODEL.datacollector.get_agent_vars_dataframe()}")
        data = globals.MODEL.datacollector.get_agent_vars_dataframe().to_json(orient='split')
        return jsonify({"columns": data['columns'], "data": data['data']}), 200
    except Exception as e:
        print(f"Error fetching agent data: {e}")
        return jsonify({'error': str(e)}), 500
    
@api.route('/api/step-once', methods=['GET'])
def step_once():
    try:
        globals.MODEL.step()
        return jsonify({'key': type(globals.MODEL.grid).__name__, 
                        'data': get_single_agent_grid_data(globals.MODEL)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Decomplexify', 
                                     description='A no code solution for Agent-based Simulation and Modeling.')
    
    # Use parse_known_args() to allow other unknown arguments from Behave
    args, unknown = parser.parse_known_args()

    # Only run the Flask app if it's not being imported by Behave
    if not unknown:  # If no extra arguments were passed, run Flask app
        api.run(host="0.0.0.0", port=3001)