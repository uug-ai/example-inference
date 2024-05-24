# Example 

This project contains an example that allows developers to retrieve media from a multitude of IP cameras in a scalable matter. This approach allows data scientists, computer vision engineers and/or machine learning experts to focus on their models and abstract the complexity of managing a IP camera network through [Kerberos.io](https://erberos.io).

An engineer will only need to install a few python models and configure the correct `environment variables` to start retreiving meda and inference with their own customised models.

## The architecture

![Kerberos Vault Integration](./assets/images/kerberos-vault-reader.png)

## Prerequisites

- Kerberos Vault
- Storage provider such as `Minio`, `S3`, `Google Storage`, `Ceph` or other S3 compliant storage.
- Message broker such as `RabbitMQ`, `Kafka`, `SQS` or any other AMQP message broker.