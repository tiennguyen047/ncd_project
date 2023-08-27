import pandas

def save_data_frame_to_csv(data_frame:pandas.DataFrame, filename:str) ->None:
    data_frame.to_csv(filename)
