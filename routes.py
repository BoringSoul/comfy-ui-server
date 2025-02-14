from starlette.routing import Mount
import task
import user

routes = [
    Mount("/api", routes=[
        Mount("/task", routes=task.routes),
        Mount("/user", routes=user.routes)
    ])
]