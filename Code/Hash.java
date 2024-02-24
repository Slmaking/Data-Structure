public class User {

    private long id;
    private String name;
    private String email;

    // standard getters/setters/constructors
        
    @Override
    public int hashCode() {
        return  1;
    }
        
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null) return false;
        if (this.getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id  
          && (name.equals(user.name)  
          && email.equals(user.email));
    }
    
    // getters and setters here
}

$$Double

public final class Double
{
private final double value;
...
public int hashCode()
{
long bits = doubleToLongBits(value);
return (int) (bits ^ (bits >>> 32));
}
}

$$Boolean

public final class Boolean
{
private final boolean value;
...
public int hashCode()
{
if (value) return 1231;
else return 1237;
}
}

$$String

public final class String
{
private final char[] s;
...
public int hashCode()
{
int hash = 0;
for (int i = 0; i < length(); i++)
hash = s[i] + (31 * hash);
return hash;
}
}
