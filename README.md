# Flash project structure example shoot from the hip

Example for separating parts of a flask project for better maintainability and scalability.

Every building block is a separate module, if needed it can contain a flask blueprint.

## Project structure

```shell
.
├── app.py
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
└── src
    ├── infrastructure
    │   └── cache.py
    ├── letters
    │   ├── blueprint.py
    │   ├── controller.py
    │   ├── repository.py
    │   └── service.py
    ├── numbers
    │   ├── blueprint.py
    │   ├── controller.py
    │   ├── repository.py
    │   └── service.py
    └── welcome
        ├── blueprint.py
        ├── controller.py
        └── templates
            └── index.html
```

- `app.py` - Main entry point for the application.
- `letters` - Module for handling letters. Contains a blueprint, controller, repository and service.
- `numbers` - Module for handling numbers. Contains a blueprint, controller, repository and service.
- `welcome` - Module for handling the welcome page. Contains a blueprint and controller and it has a template for the index page.
- `infrastructure` - Module for handling infrastructure related things. Contains a cache module.

## Building blocks

- `Blueprint` - Defines the routes, error handling, and flask related configurations.
- `Controller` - Handles the request and response.
- `Service` - Handles the business logic.
- `Repository` - Handles the database operations.

If for example a repository module gets too big, it can be split into multiple repositories. The same goes for the service module.

Usual control flow: `Blueprint` -> `Controller` -> `Service` -> `Repository`

If there is no need for a building block, it can be omitted. For example if there is no need to database interaction, there is no need for a repository. Another example is the `welcome` module, it only has a controller and a blueprint, because it only serves a static page.

## Running the application

### Local interpreter

```shell
make dev-build dev-run
```

### Docker

```shell
make build run
```

Stopping the application, and removing the container:

```shell
make stop clean
```

## Quality check

### Local interpreter

```shell
make dev-format dev-lint
```

### Docker

```shell
make format-check lint
```
