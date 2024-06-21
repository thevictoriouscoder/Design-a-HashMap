Initial intuition:

Create a list with max(float('inf')) spaces, this ensures all keys can be inserted without any chance of collision. However, this is a failure because in python, hash() is unbounded and by doing so, it creates a lot of space which causes very bad performance if a lot of slots in the list are unoccupied.

Second version:
Create a hashMap with chaining by modding the hash values of the keys by size 30(In the problem descriptions, the hashmaps are assumed to be small with at most 30 keys):

Problem with this:
Notice a lot of collisions after inserting hashes of the keys, this can significantly increase the time when searching for an element in a specific key, can optimize with linear probing to reduce collisions

![Screenshot 2024-06-20 at 5 30 45 PM](https://github.com/thevictoriouscoder/Design-a-HashMap/assets/170362161/34602225-c98a-4080-9341-c30b872e07ab)

Third version:
By implementing linear probing approach, the number of collisions drastically decreases

![Screenshot 2024-06-20 at 5 34 59 PM](https://github.com/thevictoriouscoder/Design-a-HashMap/assets/170362161/9cb3d70b-53e4-46a1-9344-941256e0c1f5)
