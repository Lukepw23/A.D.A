import json

# {
#   "family name": "",
#   "num of members": 0,
#   "members": [
#     {"role": "",
#      "name": ""
#     },
#  ]
# }

def new_family(familyName): # COMPLETED

    try:

        with open("profile_directory/family_directory.json", "r") as directory:
            data = json.load(directory)

            data["families"].append({"family name": f"{familyName}", "num of members": 0, "members": []})
            data["num of families"] += 1

        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "new family created"
    
    except:

        return "family creation failed"

def delete_family(familyName): # COMPLETED

    try:

        with open("profile_directory/family_directory.json", "r") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == familyName:
                    data["families"].remove(family)
                    data["num of families"] -= 1
        
        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "family deleted"
    
    except:

        return "family deletion failed"

def change_family_name(oldName, newName): # COMPLETED

    try:

        with open("profile_directory/family_directory.json", "r") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == oldName:
                    family["family name"] = newName
        
        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "family name changed successfully"
    
    except:

        return "family name change failed"

def add_family_member(familyName, profileName):

    try:

        with open("profile_directory/family_directory.json") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == familyName:
                    family["members"].append({"role": "", "name": f"{profileName}"})
                    family["num of members"] += 1

        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "family member added"
    
    except:

        return "family member addition failed"

def remove_family_member(familyName, profileName):

    try:

        with open("profile_directory/family_directory.json") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == familyName:
                    for member in family["members"]:
                        if member["name"] == profileName:
                            family["members"].remove(member)
                            family["num of members"] -= 1

        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "family member successfully removed"
    
    except:

        return "family member removal failed"

def move_family_member(profileName, oldFamilyName, newFamilyName):

    try:

        with open("profile_directory/family_directory.json") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == oldFamilyName:
                    for member in family["members"]:
                        if member["name"] == profileName:
                            profileObject = member
                            family["members"].remove(member)
            
            for family in data["families"]:
                if family["family name"] == newFamilyName:
                    family["members"].append(profileObject)
                            
        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)
        
        return "family member moved"
    
    except:

        return "family member move failed"

def edit_member_role(profileName, familyName, newRole):

    try:

        with open("profile_directory/family_directory.json") as directory:
            data = json.load(directory)

            for family in data["families"]:
                if family["family name"] == familyName:
                    for member in family["members"]:
                        if member["name"] == profileName:
                            member["role"] = newRole

        with open("profile_directory/family_directory.json", "w") as directory:
            json.dump(data, directory, indent = 2)

        return "member role changed"
    
    except:

        return "member role change failed"

def main():
    # with open("profile_directory/family_directory.json") as directory:
    #     data = json.load(directory)
    
    # for family in data["families"]:
    #     print(family["family name"])
    #     for member in family["members"]:
    #         print(member["role"])
    #         print(member["name"])

    edit_member_role("profile_directory/luke_williams", "williams", "son")

main()