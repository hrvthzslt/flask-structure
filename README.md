# Flask project structure example shoot from the hip

Example for separating parts of a flask project for better maintainability and scalability in an aggressively simple way.

This idea is based upon slicing your application with blueprints, but that topic is not detailed here, this is only about the additional separation of building blocks.

_Prepare yourself for a world of simplicity and free yourself from the horrors of mental overhead, let's hit the monolith road like it's 2010._

## Project description

This is a simple flask project, with endpoints that can store and list numbers and letters.

List numbers:

```shell
curl -X GET http://127.0.0.1:5000/numbers/
{
  "numbers": [
    123
  ]
}
```

Store number, and get number list:

```shell
curl -X POST http://127.0.0.1:5000/numbers/42
{
  "numbers": [
    123,
    42
  ]
}
```

This is the same for letters. I would prefer to use a standard like REST or JSON API, but this is a simple example, and this way you can easily try it.

The project has a (you're) welcome page as well for serving a static html file, for the examples sake.

The whole thing is sort of silly, but it is a good example for a project structure.

## Project structure

```shell
.
├── app.py
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
└── src
    ├── common
    │   └── infrastructure
    │       └── cache.py
    ├── letters
    │   ├── blueprint.py
    │   ├── controller.py
    │   ├── repository.py
    │   └── service.py
    ├── numbers
    │   ├── blueprint.py
    │   ├── controller
    │   │   ├── add_controller.py
    │   │   └── list_controller.py
    │   ├── error_handler.py
    │   ├── repository.py
    │   └── service
    │       ├── numbers_service.py
    │       └── validator.py
    ├── unique
    │   ├── adapter.py
    │   ├── blueprint.py
    │   ├── controller.py
    │   └── service.py
    └── welcome
        ├── blueprint.py
        ├── controller.py
        └── templates
            └── index.html
```

- `app.py` - Main entry point for the application.
- `letters` - Package for handling letters. Contains a blueprint, controller, repository and service modules.
- `numbers` - Package for handling numbers. Contains a blueprint, controller, repository and service modules.
- `welcome` - Package for handling the welcome page. Contains a blueprint and controller and it has a template for the index page.
- `common` - Package for handling project wide needs for example infrastructure related things. Contains a cache module.

## Building blocks

This is a basic example for a layered structure, where the building blocks are separated by domains.

- `Blueprint` - Defines the routes, error handling, and flask related configurations.
- `Controller` - Handles the request and response.
- `Service` - Handles the business logic.
- `Repository` - Handles the database operations.
- `Adapter` - Handles the external domain operations.

Usual relation between building blocks: `Blueprint` <- `Controller` <- `Service` <- `Repository`

**Use only what you need!**

If there is no need for a building block, it can be omitted. For example if there is no need to database interaction, there is no need for a repository. An example is the `welcome` package, it only has a controller and a blueprint, because it only serves a static page.

This statement is true for flask tools as well, `welcome` package has templates, but the others don't. Everybody has a blueprint, but `infrastructure` package doesn't need one. Speaking of not needing, a package can be only a simple package without the layers, chill.

**Split up the fat!**

When a module gets too big, it can be split into multiple modules under a package. The `numbers` controller is splat into multiple controllers, an `add_controller` and a `list_controller`, and the `error_handler` is moved to a separated module. The service module is splat into multiple services, for example a `numbers_service` and a `validator`.

**Beware of where you connect!**

If there is a need for a functionality project wide, it should be in the `common` package. For example a cache module, that is used by multiple services.

For another domain's functionality, use an adapter. For example the `unique` package has an adapter, that uses the `numbers` and `letters` services, for creating a unique list of all the values. If there is a need for a type from another domain, I personally would not a transformation without meaningful change, but you do you.

## The moral

The important thing is to make any separation by domain. Don't collect all your building blocks per one package (like a project wide controllers), because it will be harder to maintain and scale and review and refactor and staying sober and going to family dinners and... you get the point.

The names of your building blocks doesn't matter, if you think layered structure should have other layers, **do it**, if you need read/write separation, **do it** ...as long as it is separated by domains.

**But** when you decided what will your building blocks be, **stick to it**, if you choose layered architecture, don't create another module with an action-domain-responder structure (although you should check it out). So you don't have to think about the structure, and you'll have the energy to take care about the business logic. You know, the important part.

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
