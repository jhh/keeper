SELECT t.time, u.*
FROM trapper_action a, trapper_trace t, unnest(a.measures, t.data) AS u(measure, value)
WHERE a.id = t.action_id AND a.created_at = (SELECT max(created_at) FROM trapper_action);