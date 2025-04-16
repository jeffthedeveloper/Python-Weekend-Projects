from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def check_database_connection(db: AsyncSession) -> str:
    """
    Check if database connection is working
    
    Args:
        db: Database session
        
    Returns:
        str: Status message ("connected" or "disconnected")
    """
    try:
        await db.execute(text("SELECT 1"))
        return "connected"
    except Exception as e:
        return f"disconnected: {str(e)}"