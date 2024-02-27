# AI Junior Developer Test 

# Architecture 
![alt text](https://github.com/amankushwaha25/OpenFabric-Assessment/blob/master/flowchart.jpeg)

# Approach
- Fine tune DistillBERT LLM over Q&A daatset.
- Push the model to the hub
- Call the model to generate answers for the question.
- If response generated is good then all OK!!, otherwise finetune the model again on the question.

# Run
- clone the repository in your local system.
- Install docker in your system.
- Navigate to the folder where the repository is cloned.
- Use the build command `docker build .`
- after successful build, run command docker images to get the name of the docker image created
- Run the command `docker run -p 5500:5500 <image_name>`
- Open browser and go to the link `http://localhost:5500/`
 
# Run using the shell script
- Clone the repository in your local system.
- Navigate to the folder where the repository is cloned.
- Run the `start.sh` file.

# Demo Link
https://drive.google.com/file/d/1lgsl4ZrIJRo8BVBtO6PtkG9N1en3e-c7/view?usp=sharing
