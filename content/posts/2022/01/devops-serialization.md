Title: JSON/BSON Serialization in Golang
Slug: devops-serialization
Date: 2022-01-16 00:00
Category: Coding
Tags: programming, golang, serialization

I am building a messaging system. The code for this messaging system is located at a Bitbucket [repository](https://bitbucket.org/yyongche/devops/src/master/). The provided instructions allow this messaging system to be run standalone in a self-hosted Kubernetes cluster.

The messaging system provides a REST API in JSON and saves/loads messages in MongoDB using BSON. Struct Tags in the Go programming language make the JSON/BSON serialization a much clearer and concise implementation.

```
type MessageHeader struct {
	ID        primitive.ObjectID `json:"-" bson:"_id"`
	CreatedAt time.Time          `json:"created_at" bson:"created_at"`
	User      string             `json:"user" bson:"user"`
	Url       string             `json:"url" bson:"-"`
}

type Message struct {
	ID        primitive.ObjectID `json:"-" bson:"_id"`
	CreatedAt time.Time          `json:"created_at" bson:"created_at"`
	User      string             `json:"user" bson:"user"`
	Content   string             `json:"content" bson:"content"`
}
```

The `json:"-"` and `bson:"-"` tags are used to ignore a field during the JSON/BSON serialization.
