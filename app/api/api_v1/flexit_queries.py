from fastapi import APIRouter, HTTPException

from flexit import queries

router = APIRouter()


@router.get("/shows_of_actor")
async def shows_of_actor(actor: str):
    """Call shows_of_actor flexit query."""
    try:
        return queries.shows_of_actor(actor)
    except ValueError:
        raise HTTPException(
            status_code=404, detail=f"{actor} was not found in any shows!"
        )


@router.get("/shows_in_category")
async def shows_in_category(category: str, start: int = 0, stop: int = 20):
    """Call shows_in_category flexit query."""
    if start > stop:
        raise HTTPException(
            status_code=422, detail="value of start must be less than value of stop."
        )
    try:
        return queries.shows_in_category(category, start, stop)
    except NotImplementedError:
        raise HTTPException(
            status_code=422, detail="range between start and stop must be below 100."
        )


@router.get("/person_is_director_and_actor")
async def person_is_director_and_actor(person: str):
    """Call person_is_director_and_actor flexit query."""
    try:
        return queries.person_is_director_and_actor(person)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail=f"{person} is not in database, and therefore not an actor or director.",
        )


@router.get("/person_directed_and_acted_in_same_show")
async def person_directed_and_acted_in_same_show(person: str):
    """Call queries.person_directed_and_acted_in_same_show flexit query."""
    try:
        return queries.person_directed_and_acted_in_same_show(person)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail=f"{person} is not in database, and therefore not an actor or director.",
        )


@router.get("/shows_added_on_date")
async def shows_added_on_date(date):
    """Call queries.shows_added_on_date flexit query."""
    return queries.shows_added_on_date(date)


@router.get("/high_level_stats")
async def high_level_stats():
    """Call queries.high_level_stats flexit query."""
    return queries.high_level_stats()
