def analyze_user_activity(log_file_path: str) -> dict:
    users = set()
    action_counts = {}
    user_durations = {}
    login_durations = []

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                
                if len(parts) != 4:
                    continue
                    
                timestamp, user_id, action, duration_str = parts
                
                try:
                    duration = float(duration_str)
                except ValueError:
                    continue
                    
                users.add(user_id)
                
                action_counts[action] = action_counts.get(action, 0) + 1
                
                user_durations[user_id] = user_durations.get(user_id, 0.0) + duration
                
                if action == 'login':
                    login_durations.append(duration)
                    
    except FileNotFoundError:
        pass
        
    most_active_user = max(user_durations, key=user_durations.get) if user_durations else None
    
    average_session_time = sum(login_durations) / len(login_durations) if login_durations else 0.0

    return {
        "total_users": len(users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": average_session_time
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
