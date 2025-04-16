// Constraints creation (unchanged structure)
CREATE CONSTRAINT user_id IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE;
CREATE CONSTRAINT team_id IF NOT EXISTS FOR (t:Team) REQUIRE t.id IS UNIQUE;
CREATE CONSTRAINT session_id IF NOT EXISTS FOR (s:TeamChatSession) REQUIRE s.id IS UNIQUE;

// Data loading from new League of Legends dataset
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/your-repo/lol-chat-logs/main/team_chats.csv" AS row
MERGE (u:User {id: toInteger(row.userId)})
MERGE (t:Team {id: toInteger(row.teamId)})
MERGE (s:TeamChatSession {id: toInteger(row.sessionId)})
MERGE (u)-[:CREATED_SESSION {timestamp: datetime(row.timestamp)}]->(s)
MERGE (s)-[:TEAM_SESSION]->(t);