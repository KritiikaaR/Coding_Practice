import java.util.*;

public class UserLogin {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		HashMap<String,String> user =new HashMap<>();
		int choice;
		
		do {
			System.out.println("What would you like to do? ");
			System.out.println("1. Register user ");
			System.out.println("2. Search for user ");
			System.out.println("3. Reset passcode ");
			System.out.println("4. Exit ");
			choice=sc.nextInt();
			sc.nextLine();
			
			switch(choice) {
			
			case 1:
				System.out.println("Enter User ID: ");
				String userID=sc.nextLine();
				
				if (user.containsKey(userID)) {
					System.out.println("The ID is already taken. ");
				} else {
					System.out.println("Enter the password: ");
					String passcode=sc.nextLine();
					user.put(userID, passcode);
				}
				break;
				
				
			case 2:
				System.out.println("Enter User ID you want to search for: ");
				String uID=sc.nextLine();
				
				if (user.containsKey(uID)) {
					System.out.println("User found.");
					System.out.println("Would you like to see the password?(y/n) ");
					String opt=sc.nextLine();
					
					if (opt.equalsIgnoreCase("y")) {
						System.out.println(user.get(uID));
					}else {
						System.out.println("Okay.");
					}
					
				} else {
					System.out.println("User not found.");

				}
				break;
				
			case 3:
				System.out.println("Enter User ID you want to reset password for: ");
				String usID=sc.nextLine();
				
				if (user.containsKey(usID)) {
					System.out.println("User found.");
					System.out.println("Enter new password: ");
					String opt=sc.nextLine();
					
					//update the new password in the hash map
					user.put(usID,opt);
					System.out.println("Password updated.");
					
				}else {
					System.out.println("User not registered. ");
				}
				break;
				
				
			case 4:
				System.out.println("Byeeeeeeee ");
			break;
				
			default:
				System.out.println("Please enter a number between (1-4)");
			break;	
			}
			
			
		} while(choice !=4);
		
		sc.close();
	}
}
