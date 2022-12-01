# Build (make sure you are in the right directory)
- `docker build -t ubuntu .`

# Run 
- `docker run -i -d --rm ubuntu` 
- note, the -d stands for 'detached' - meaning that this will run in the background 
- if we want to see what is running in the background, we can do: `docker ps` to see list of containers running 
- if we want to jummp into the terminal of the running container: 
    - `docker exec -it 408f95b22bcf /bin/bash` - will run/execute a command, bringing up the /bash terminal for us 