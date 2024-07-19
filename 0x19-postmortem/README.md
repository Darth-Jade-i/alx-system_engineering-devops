# Postmortem: E-commerce Website Outage

## Issue Summary

Duration:
The outage lasted for 3 hours, from 10:00 AM to 1:00 PM WAT (West Africa Time) on July 15, 2024.

Impact:
The primary service affected was our e-commerce website, where users experienced slow loading times and were unable to complete purchases. Approximately 70% of users were affected, leading to a significant drop in transaction completion rates.

Root Cause:
The root cause was a misconfiguration in the database connection pool settings, which led to a bottleneck and subsequent overload of the database server.

## Timeline

- 10:00 AM: Issue detected through a monitoring alert indicating a spike in response times and error rates.
- 10:05 AM: Initial investigation began by the on-call engineer who noticed high database CPU utilization.
- 10:15 AM: Assumption made that a recent deployment might have caused the issue; rollback initiated.
- 10:30 AM: Rollback completed, but the issue persisted.
- 10:45 AM: Network latency was suspected; network team involved to check for any issues.
- 11:00 AM: Network team confirmed no issues; attention returned to the database.
- 11:15 AM: Database team engaged to perform an in-depth analysis.
- 11:30 AM: Misleading path followed by investigating possible DDoS attack; no evidence found.
- 12:00 PM: Deeper analysis revealed a high number of active connections in the database.
- 12:15 PM: Root cause identified as a misconfiguration in the database connection pool settings.
- 12:30 PM: Configuration settings corrected and applied.
- 12:45 PM: System began to stabilize; monitoring continued to ensure no recurrence.
- 1:00 PM: Full service restoration confirmed.

## Root Cause and Resolution

Root Cause:
The database connection pool settings were incorrectly configured to allow an excessive number of connections. This configuration caused the database server to become overwhelmed, leading to high CPU usage and slow query responses. The excessive connections were due to a configuration file update that had not been thoroughly tested before deployment.

Resolution:
The issue was resolved by correcting the database connection pool settings to appropriate values. The maximum number of connections was reduced to a manageable level, and the database server was restarted to apply the new settings. This alleviated the load on the database and restored normal operation.

## Corrective and Preventative Measures

Improvements:
1. Implement a more rigorous testing process for configuration changes, especially those related to critical systems like the database.
2. Enhance monitoring to include alerts for unusual spikes in database connections and CPU usage.
3. Conduct regular reviews and audits of system configurations to ensure they align with best practices and current operational needs.

TODO List:
1. Patch Nginx server: Ensure that the web server is running the latest version and has all security patches applied.
2. Add monitoring on server memory: Implement detailed monitoring for server memory usage to detect potential issues early.
3. Update database connection pool settings: Review and adjust the settings as needed to prevent future overloads.
4. Deploy configuration management tool: Use tools like Ansible or Chef to automate and manage configuration changes.
5. Run load tests on staging: Conduct regular load testing on a staging environment to validate changes before production deployment.
6. Improve incident response documentation: Create detailed runbooks and checklists for common incidents to streamline future troubleshooting efforts.

By implementing these measures, we aim to prevent similar issues from occurring in the future and ensure a more robust and resilient system.