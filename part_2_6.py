"""
Write a short docstring for the function below,
so that other people reading this code can quickly understand what this function does.

You may also rename the functions if you can think of clearer names.
"""

def step_function_maker(start_time, end_time, value):
    """ This function creates and returns a function that can be used to convert time into a step value 

    Args:
        start_time (timestamp) : start time of event
        end_time (timestamp) : end time of event
        value (float): step value
    
    Returns: 
        convert_to_step_value(function) : returns the function that will convert an input time to a step value 

    """    
    def convert_to_step_value(time):
        """ This function converts the input time into a step value 

        Args:
            time (timestamp): input timestamp that needs to be converted into a step value 

        Returns:
            y (float) : The converted step value 
        """        
        if start_time <= time <= end_time:
            y = value
        else:
            y = 0.0
        return y

    return convert_to_step_value
