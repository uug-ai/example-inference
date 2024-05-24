# Example 

This project contains an example that allows developers to retrieve media from a multitude of IP cameras in a scalable matter. This approach allows data scientists, computer vision engineers and/or machine learning experts to focus on their models and abstract the complexity of managing a IP camera network through [Kerberos.io](https://kerberos.io).

An engineer will only need to install a few python models and configure the correct `environment variables` to start retreiving meda and inference with their own customised models.

## The architecture

As you can see on following architecture, a network of IP cameras is made available in a specific network. By deploying the Kerberos.io stack: Kerberos Agent(s) and Kerberos Vault, we are able to connect and record (in chuncks) the IP camera streams, and store the relevant media on a storage provider of choice.

Once media has been successfully stored (going from Kerberos Agent) into Kerberos Vault, an integration is activated and a message created in one of the preferred message brokers. This message includes various metadata such as `filename`, `cameraid`, `timestamp` and more.

Specific python modules are made available, allowing a developer to build its own application and leverage boilerplate code to solely focus on the things that brings business value. The various python modules simplify to fetch messages from one or more queues, retrieve recording from a specific storage provider through Kerberos Vault, and various other computer vision functions and features.

![Kerberos Vault Integration](./assets/images/kerberos-vault-reader.png)

## Prerequisites

- Kerberos Vault: Have [a look here](https://doc.kerberos.io/vault/first-things-first) for a better understanding of what it's about and how to install.
- Storage provider such as `Minio`, `S3`, `Google Storage`, `Ceph` or other S3 compliant storage.
- Message broker such as `RabbitMQ`, `Kafka`, `SQS` or any other AMQP message broker.

## Let's get started

...

## Install and run

...