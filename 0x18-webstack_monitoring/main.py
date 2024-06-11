{
    "id": 146770375,
    "name": "High Read Requests on Device",
    "type": "query alert",
    "query": "avg(last_5m):avg:system.load.1{host:429651-web-01} by {host} > 100",
    "message": "<!--StartFragment-->\n\nHigh Read Requests on Device\n\n<!--EndFragment-->",
    "tags": [],
    "options": {
        "thresholds": {"critical": 100},
        "notify_audit": false,
        "include_tags": true,
        "new_group_delay": 60,
        "notify_no_data": false,
        "silenced": {},
    },
    "priority": null,
    "restricted_roles": null,
}
