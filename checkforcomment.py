import boto.ec2
from boto.manage.cmdshell import sshclient_from_instance
import time
import praw

# Connect to your region of choice
conn = boto.ec2.connect_to_region('us-east-1')
print(conn)
# Find the instance object related to my instanceId
instance = conn.get_all_instances(['i-3dc50e2a'])[0].instances[0]
print(instance)
# Create an SSH client for our instance
#    key_path is the path to the SSH private key associated with instance
#    user_name is the user to login as on the instance (e.g. ubuntu, ec2-user, etc.)
ssh_client = sshclient_from_instance(instance,
                                     'birdman.pem',
                                     user_name='ubuntu')
reddit = praw.Reddit(user_agent="Python/TensorFlow: Seq2Seq Chat (by /u/yadayada1212)",client_id='M9qNqXnuHbDs8w',
	client_secret='UL0odj8bpIft91claCnXemPkFTI',username='yadayada1212',password='yoloyolo1212')
# replace '' with text, which will represent the seq2seq data
subreddit = reddit.subreddit('BlueLobster')
op = reddit.redditor('yadayada1212')

for comment in subreddit.stream.comments():
	if comment.author != op:
		# Run the command. Returns a tuple consisting of:
		#    The integer status of the command
		#    A string containing the output of the command
		#    A string containing the stderr output of the command
		# status, stdout, stderr = ssh_client.run(' ./tf_seq2seq_chatbot/tf_seq2seq_chatbot/data/test/')
		
		status, stdout, stderr = ssh_client.run('echo "Do you like pizza?" > "tf_seq2seq_chatbot/tf_seq2seq_chatbot/data/test/test_set.txt"')
		status, stdout, stderr = ssh_client.run('python ~/tf_seq2seq_chatbot/test.py')
		# print(stdout)
		# print(stdout.split("FINALSTR123")) 
		text = str(stdout).split("FINALSTR123")[1]
		comment.reply(text)
		print(text)