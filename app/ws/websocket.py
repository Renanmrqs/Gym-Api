from fastapi import APIRouter, Depends,  WebSocket, WebSocketDisconnect
from app.ws.manager import manager

router = APIRouter()

@router.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Message text was: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
