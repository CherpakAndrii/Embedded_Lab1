from app.interfaces.agent_gateway import AgentGateway


class AgentMQTTAdapter(AgentGateway):
    def on_message(self, client, userdata, msg):
        """
        Method to handle incoming messages from the agent.
        Parameters:
            client: MQTT client instance.
            userdata: Any additional user data passed to the MQTT client.
            msg: The MQTT message received from the agent.
        """
        pass

    def connect(self):
        """
        Method to establish a connection to the agent.
        """
        pass

    def start(self):
        """
        Method to start listening for messages from the agent.
        """
        pass

    def stop(self):
        """
        Method to stop the agent gateway and clean up resources.
        """
        pass
