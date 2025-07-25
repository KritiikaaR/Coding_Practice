import java.text.NumberFormat;
import java.util.Scanner;

class Productt {
    private String code;
    private String description;
    private double price;
    protected static int count = 0;

    public Productt()
    {
        code = "";
        description = "";
        price = 0;
    }

    public void setCode(String code)
    {
        this.code = code;
    }

    public String getCode(){
        return code;
    }

    public void setDescription(String description)
    {
        this.description = description;
    }

    public String getDescription()
    {
        return description;
    }

    public void setPrice(double price)
    {
        this.price = price;
    }

    public double getPrice()
    {
        return price;
    }

    public String getFormattedPrice()
    {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        return currency.format(price);
    }

    public String toString()
    {
        return "Code:        " + code + "\n" +
               "Description: " + description + "\n" +
               "Price:       " + this.getFormattedPrice() + "\n";
    }

    public static int getCount()
    {
        return count;
    }
}

class Book extends Productt{
	private String author;
	
	public Book(){
		super();
		author = "";
		count++;
    }

	public void setAuthor(String author){
		this.author = author;
	}

	public String getAuthor(){
		return author;
	}

	public String toString(){
		return super.toString() + "Author:      " + author + "\n";
	}
}

class Software extends Productt{
	private String version;
	
	public Software(){
		super();
		version = "";
		count++;
	}
	
	public void setVersion(String version){
		this.version = version;
	}
	
	public String getVersion(){
		return version;
	}
	
	public String toString(){
		return super.toString() +"Version:     " + version + "\n";
	}
}

class CompactDisc extends Productt{
	private String artist;
	
	public CompactDisc() {
		super();
		artist="";
		count++;
	}
	
	public void setArtist(String artist) {
		this.artist=artist;
	}
	public String getArtist() {
		return artist;
	}
	
	
	public String toString(){
		return super.toString() +"Artist:     " + artist + "\n";
	}
	
	
}

class ProductDB{
    public static Productt getProduct(String productCode) {
        // In a more realistic application, this code would
        // get the data for the product from a file or database
        // For now, this code just uses if/else statements
        // to return the correct product data

        Productt p = null;

        if (productCode.equalsIgnoreCase("java") ||
           productCode.equalsIgnoreCase("jsps") ||
           productCode.equalsIgnoreCase("mcb2"))
        {
            Book b = new Book();
            if (productCode.equalsIgnoreCase("java"))
            {
                b.setCode(productCode);
                b.setDescription("Murach's Beginning Java 2");
                b.setPrice(49.50);
                b.setAuthor("Andrea Steelman");
            }
            else if (productCode.equalsIgnoreCase("jsps"))
            {
                b.setCode(productCode);
                b.setDescription("Murach's Java Servlets and JSP");
                b.setPrice(49.50);
                b.setAuthor("Andrea Steelman");
            }
            else if (productCode.equalsIgnoreCase("mcb2"))
            {
                b.setCode(productCode);
                b.setDescription("Murach's Mainframe COBOL");
                b.setPrice(59.50);
                b.setAuthor("Mike Murach");
            }
            p = b; // set Product object equal to the Book object
        
        } else if (productCode.equalsIgnoreCase("txtp")){
            Software s = new Software();
            s.setCode("txtp");
            s.setDescription("TextPad");
            s.setPrice(27.00);
            s.setVersion("4.7.3");
            p = s; // set Product object equal to the Software object
        
        } else if (productCode.equalsIgnoreCase("sgtp")) {
        	CompactDisc cd=new CompactDisc();
        	cd.setCode("sgtp");
        	cd.setDescription("Sgt. Pepper's Lonely Hearts Club Band");
        	cd.setPrice(15.00);
        	cd.setArtist("The Beatles");
        	p=cd;
        }
        return p;
    }
}



public class ProductApp{
    public static void main(String args[]){
        // display a welcome message
        System.out.println("Welcome to the Product Selector\n");

        // perform 1 or more selections
        Scanner sc = new Scanner(System.in);
        String choice = "y";
        while (choice.equalsIgnoreCase("y"))
        {
            System.out.print("Enter product code: ");
            String productCode = sc.next();  // read the product code
            sc.nextLine();  // discard any other data entered on the line

            // get the Product object
            Productt p = ProductDB.getProduct(productCode);

            // display the output
            System.out.println();
            if (p != null)
                System.out.println(p.toString());
            else
                System.out.println("No product matches this product code.\n");

            System.out.println("Product count: " + Productt.getCount() + "\n");

            // see if the user wants to continue
            System.out.print("Continue? (y/n): ");
            choice = sc.nextLine();
            System.out.println(); 
        }
        sc.close();
    }
}