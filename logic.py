def analyze_behavior(speed, acceleration, braking):
    return (speed/100 + acceleration/5 + braking/5) / 3

def calculate_risk_score(behavior_score):
    return round(behavior_score * 100, 2)

def calculate_premium(risk_score):
    base = 5000
    return round(base + (risk_score/100 * base), 2)

def generate_feedback(risk_score):
    if risk_score > 80:
        return "High risk: Reduce speed and sudden braking."
    elif risk_score > 50:
        return "Moderate risk: Drive cautiously."
    else:
        return "Low risk: Good driving behavior."
