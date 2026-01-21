from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user(session: AsyncSession, user_id: int):
    """Fetch a user by ID"""
    result = await session.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def get_all_users(session: AsyncSession):
    """Fetch all users"""
    result = await session.execute(select(User))
    return result.scalars().all()