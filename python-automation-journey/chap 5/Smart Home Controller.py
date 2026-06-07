# User se smart home ki command input lena aur use small letters mein badalna
devices = input("Say a command (e.g., 'ac on', 'party mode'): ").lower()

# 'match' statement shuru ho rahi hai jo 'command' ko check karegi
match devices:
    
    # Agar user ne likha "turn on lights" ya "lights on"
    case "turn on lights" | "lights on":
        print("💡 Lights turned ON. Room brightness set to 100%.")
        
    # Agar user ne likha "turn off lights" ya "lights off"
    case "turn off lights" | "lights off":
        print("🌑 Lights turned OFF. Goodnight!")
        
    # Security command
    case "lock doors":
        print("🔒 All main doors and windows are now SECURELY LOCKED.")
        
    # AC control command
    case "ac on":
        print("❄️ AC is turned ON. Temperature set to 24°C.")
        
    # Special Scene: Party Mode
    case "party mode":
        print("🥳 Party Mode Activated!")
        print("🌈 Disco lights ON | 🎵 Music Volume set to 80% | 🥤 Fridge cooling increased!")
        
    # Special Scene: Good Night
    case "good night":
        print("🌙 Good Night Mode Activated.")
        print("🔒 Doors Locked | 🌑 Lights OFF | ❄️ AC set to 26°C | ⏰ Alarm set for 7:00 AM.")
        
    # Default Case (_): Agar upar wali koi bhi command match NAHI hui (Pichle mcq wala logic!)
    case _:
        print("❌ Sorry, I didn't understand that command. Please say something like 'party mode' or 'ac on'.")