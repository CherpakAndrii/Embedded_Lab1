from typing import List

from fastapi import APIRouter

from models import ProcessedAgentData
from database import ProcessedAgentDataInDB, session

processed_agent_data_router = APIRouter()


@processed_agent_data_router.post("/")
async def create_processed_agent_data(data: List[ProcessedAgentData]):
    session.bulk_save_objects(
        [ProcessedAgentDataInDB(
            road_state=a_data.road_state,
            user_id=a_data.agent_data.user_id,
            x=a_data.agent_data.accelerometer.x,
            y=a_data.agent_data.accelerometer.y,
            z=a_data.agent_data.accelerometer.z,
            latitude=a_data.agent_data.gps.latitude,
            longitude=a_data.agent_data.gps.longitude,
            timestamp=a_data.agent_data.timestamp
        ) for a_data in data]
    )
    session.commit()
    return


@processed_agent_data_router.get("/{processed_agent_data_id}")
def read_processed_agent_data(processed_agent_data_id: int):
    return session.query(ProcessedAgentDataInDB).get(processed_agent_data_id)


@processed_agent_data_router.get("/")
def list_processed_agent_data():
    return list(session.query(ProcessedAgentDataInDB).all())


@processed_agent_data_router.put("/{processed_agent_data_id}")
def update_processed_agent_data(processed_agent_data_id: int, data: ProcessedAgentData):
    updated_instance = ProcessedAgentDataInDB(
            road_state=data.road_state,
            user_id=data.agent_data.user_id,
            x=data.agent_data.accelerometer.x,
            y=data.agent_data.accelerometer.y,
            z=data.agent_data.accelerometer.z,
            latitude=data.agent_data.gps.latitude,
            longitude=data.agent_data.gps.longitude,
            timestamp=data.agent_data.timestamp,
            id=processed_agent_data_id
        )

    session.merge(updated_instance)
    session.commit()
    return updated_instance


@processed_agent_data_router.delete("/{processed_agent_data_id}")
def delete_processed_agent_data(processed_agent_data_id: int):
    obj = session.query(ProcessedAgentDataInDB).get(processed_agent_data_id)
    session.delete(obj)
    session.commit()
    return obj


@processed_agent_data_router.delete("/")
def clear_all_data():
    data = session.query(ProcessedAgentDataInDB)
    lines_count = data.count()
    data.delete()
    session.commit()
    return {"lines_deleted": lines_count}
