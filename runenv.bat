IF EXIST .env_process (
    CALL .env\scripts\deactivate
    del .env_process
) ELSE (
    CALL .env\scripts\activate
    type NUL > .env_process
)
