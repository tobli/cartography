DESCRIBE_KEY_PAIRS = {
    "KeyPairs": [
        {
            "KeyFingerprint": "11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11:11",
            "KeyName": "sample_key_pair_1",
        },
        {
            "KeyFingerprint": "22:22:22:22:22:22:22:22:22:22:22:22:22:22:22:22:22:22:22:22",
            "KeyName": "sample_key_pair_2",
        },
        {
            "KeyFingerprint": "33:33:33:33:33:33:33:33:33:33:33:33:33:33:33:33:33:33:33:33",
            "KeyName": "sample_key_pair_3",
        },
    ],
}


DESCRIBE_TAGS = {
    "Tags": [
        {
            "ResourceType": "instance",
            "ResourceId": "tagged-instance",
            "Value": "foo",
            "Key": "Name",
        },
        {
            "ResourceType": "network-interface",
            "ResourceId": "tagged-network-interface",
            "Value": "bar",
            "Key": "Name",
        },
        {
            "ResourceType": "security-group",
            "ResourceId": "tagged-security-group",
            "Value": "High",
            "Key": "Importance",
        },
        {
            "ResourceType": "subnet",
            "ResourceId": "tagged-subnet",
            "Value": "Test",
            "Key": "Environment",
        },
        {
            "ResourceType": "vpc",
            "ResourceId": "tagged-vpc",
            "Value": "Private",
            "Key": "Name",
        },
    ],
}
