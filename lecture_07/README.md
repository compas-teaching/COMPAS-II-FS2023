# COMPAS II: Assembly of discrete elements II

Applied exercise from design to planning fabrication for an assembly of discrete elements.

## Examples

* [Pick and Place planning and control](700-pick-and-place-control.ghx)

Make sure you start (`compose up`) the container before running the example. There are 3 docker compose files available now:

  * `docker-compose.yml`: the default one, is configured by default to connect to RobotStudio virtual controller
  * `docker-compose.real-robot.yml`: same as previous, but configured to connect to the service port of a real robot controller.
  * `docker-compose-bioik.yml`: based on a new release of the docker images, it contains a new IK solver called [bio-ik](https://tams-group.github.io/bio_ik/). 
