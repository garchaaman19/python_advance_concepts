## Exchange type 
1. Direct Exchange: 
    - Routes messages to a queue based on an exact match between the routing key and the binding key.
    - Example: Routing key info matches a queue bound to the info binding key.

2. Fanout Exchange
    - Broadcasts messages to all bound queues, ignoring the routing key.

3. Topic 
    - Routes messages based on wildcard patterns in the routing key.



## Dead Letter Exchange (DLX)
- Handles messages that are rejected, expired (TTL), or not routable.

