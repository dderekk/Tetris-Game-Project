import pandas as pd
from blockControl import BlocksControl

class dataProcess:
    """process data, fetch data from excel, update data, get score, update block data"""

    def __init__(self):
        """initialization"""
        self.name = None
        self.score = None

    def featchNewScore(self):
        """get data from excel or csv"""
        data = pd.read_csv('climate.csv')

        self.name= data['name'].tolist()
        self.score = data['score'].tolist()

    def getTop10Data(self):
        """select top 10 score,
        output name and score in list"""
        self.featchNewScore()
        zipped = list(zip(self.name, self.score))

        sorted_data = sorted(zipped, key=lambda x: x[1], reverse=True)  # 从大到小排序
        return(sorted_data[:10])

    def getBlockData(self,block):
        """return the block background"""
        #return the block diagram as → [0,0,0,1...]
        return block.background

    def checkHighScore(self,score):
        """check if the new score is top 10"""
        numberTen = self.getTop10Data()[-1][-1]
        if score > numberTen:
            return True
        else:
            return False

    def addNewData(self, new_name, new_score):
        """add new data, input player name and current score"""
        # Read the existing CSV into a DataFrame
        data = pd.read_csv('climate.csv')

        # Check if the name already exists in the DataFrame
        if new_name in data['name'].values:
            # Find the row index where the name matches
            index = data[data['name'] == new_name].index[0]

            # Check if the new score is higher than the existing score
            if new_score > data.at[index, 'score']:
                # Update the score with the new score
                data.at[index, 'score'] = new_score
        else:
            # Create a new DataFrame with the new data
            new_data = pd.DataFrame({'name': [new_name], 'score': [new_score]})

            # Concatenate the existing data and the new data
            data = pd.concat([data, new_data], ignore_index=True)

        # Save the updated DataFrame back to the CSV file
        data.to_csv('climate.csv', index=False)
