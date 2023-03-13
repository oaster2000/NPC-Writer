import os, requests, json

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class World:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Anvil:
    current_world: World
    
    def __init__(self):
        self.auth_token = os.getenv("WA_USER_TOKEN")
        self.application_key = os.getenv("WA_APPLICATION_KEY")
        self.headers = {
            "x-auth-token": self.auth_token,
            "x-application-key": self.application_key,
            "Content-type": "application/json",
            "User-Agent": "Web App v0.1"
        }
        self.current_world = World("", "")

    def load_user(self):
        url = "https://www.worldanvil.com/api/aragorn/user"
        response = requests.get(url, headers=self.headers)
        result = json.loads(response.text)
        return User(result["id"], result["username"])
    
    def load_worlds(self, user):
        url = "https://www.worldanvil.com/api/aragorn/user/" + user.id + "/worlds"
        response = requests.get(url, headers=self.headers)
        result = json.loads(response.text)
        worlds = []
        for world in result["worlds"]:
            worlds.append(World(world["id"], world["name"]))
        return worlds
    
    def get_world(self, worlds, world_id):
        for world in worlds:
            if world.id == world_id:
                return world
            
        return None