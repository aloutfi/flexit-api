from fastapi import APIRouter, HTTPException

from flexit import creation, queries, dto

router = APIRouter(tags=["flexit queries"])


@router.get("/high-level-stats")
async def high_level_stats():
    """Some high level statistics about the dataset."""
    return queries.high_level_stats()


@router.get("/shows-of-actor")
async def shows_of_actor(actor: str):
    """Query the database for shows that an actor has participated in as a cast member."""
    try:
        return queries.shows_of_actor(actor)
    except ValueError:
        raise HTTPException(
            status_code=404, detail=f"{actor} was not found in any shows!"
        )


@router.get("/shows-in-category")
async def shows_in_category(category: str, start: int = 0, stop: int = 20):
    """Query the database for shows that fall within a given category. You can call up to 99 values at once."""
    if start > stop:
        raise HTTPException(
            status_code=422, detail="value of start must be less than value of stop."
        )
    try:
        return queries.shows_in_category(category, start, stop)
    except ValueError:
        raise HTTPException(
            status_code=404, detail="The category doesn't exist in our database."
        )
    except NotImplementedError:
        raise HTTPException(
            status_code=422, detail="range between start and stop must be below 100."
        )


@router.get("/person-is-director-and-actor")
async def person_is_director_and_actor(person: str):
    """Query the database to determine whether a person has directed and acted."""
    try:
        return queries.person_is_director_and_actor(person)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail=f"{person} is not in database, and therefore not an actor or director.",
        )


@router.get("/person-directed-and-acted-in-same-show")
async def person_directed_and_acted_in_same_show(person: str):
    """Query the database for shows that a person was both a director for and a cast member of."""
    try:
        return queries.person_directed_and_acted_in_same_show(person)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail=f"{person} is not in database, and therefore not an actor or director.",
        )


@router.get("/shows-added-on-date")
async def shows_added_on_date(date: str):
    """Query the database for shows that were added on a specific date."""
    return queries.shows_added_on_date(date)


@router.post("/add-show-to-database")
async def add_show_to_database(show: dto.Show):
    """Add a new show to the database!"""
    return creation.create_show(show)
