cd /
psql db -U dbuser -c "ALTER USER dbuser WITH PASSWORD '$(cat /run/secrets/db_password | sed -n 's/^dbpass = "\(.*\)"$/\1/p')';"