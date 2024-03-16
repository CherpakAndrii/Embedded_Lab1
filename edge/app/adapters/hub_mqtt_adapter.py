from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.hub_gateway import HubGateway


class HubMqttAdapter(HubGateway):
    def save_data(self, processed_data: ProcessedAgentData) -> bool:
        """
        Method to save the processed agent data in the database.
        Parameters:
            processed_data (ProcessedAgentData): The processed agent data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        pass
