This README guides you through building a Docker image and deploying the laban.gg web app to Kubernetes. laban.gg is a website designed to serve as a hub for fighting game tournaments in the Philippines.

Before starting, ensure you have the following:
Docker installed and configured.
Access to Google Cloud and a working Kubernetes cluster on Google Cloud.
kubectl installed and connected to your Google Cloud project.

Here are test credentials to be used on the website itself:

Tournament Attendee Account
Username: 2
Password: 3

Tournament Organizer Account
Username: 3
Password: 3

Clone this repository and navigate to its directory in your terminal:
git clone https://github.com/SpokBlok/ISCS-30.23-Containerizing
cd ISCS-30.23-Containerizing

And then, run these lines
docker build -t <dockerhub-username>/<image-name>:<tag> .
docker push <dockerhub-username>/<image-name>:<tag>

This should create a docker image and push it to docker hub.
To test that it works, run this line
docker run -p 8080:8080 <dockerhub-username>/<image-name>:<tag>
and go to localhost:8080. It should lead you to the register account page.

Next step would be to go to the Kubernetes tab in Google Cloud ad create a new cluster.
Then, click on Create and select the Autopilot cluster.
Change the name and region to your liking, and leave every other setting to default.

Once that is done, click on the Google Cloud Console and upload the kubernetes-manifests folder to the console.
And then, once you're in the direectory of the folder, run this line
kubectl apply -f .

To double check that they've been created successfully, run the following lines

kubectl get pods
kubectl get svc
kubectl get ingress

After waiting a while, run this line again
kubectl get ingress
and get the address under the ADDRESS tab.

If you place this address in your browser, it should lead to the deployed laban.gg.