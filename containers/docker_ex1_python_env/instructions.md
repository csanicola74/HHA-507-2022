# Simple example 

## Install docker 
- https://docs.docker.com/get-docker/

## Post-installation
- Make sure it works by running following command:
    - `docker run hello-world` 

## To run this docker file: 
- First run build command: `docker build -t example1 .`

## Check that the image was built
- `docker images` - can also see the file sizes 

- Then can run it: `docker run -it --rm example1` 
    - (-it) keeps the container running 
    - (--rm) automatically removes the container when exiting the program 