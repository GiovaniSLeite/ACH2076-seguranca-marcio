import java.util.Random;
import java.util.Arrays;
import java.security.SecureRandom;
import java.util.BitSet;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
public class Geradores {

	static int SIZE = 1000000;
	public static void main(String[] args){
		System.out.println("Random_secure");
		write("random_secure.pi", random_secure());
		System.out.println("Random_standart");
		write("random_standart.pi", random_standart());
	}

	public static String random_standart(){
		Random random = new Random();
		String s = "";
		for(int i = 0; i < SIZE; i++){
			System.out.println("Caracter " + i);
			s = s + "" + random.nextInt(2);
		}
		return s;
	}

	public static String random_secure(){
		SecureRandom s = new SecureRandom();
		byte[] seed = new byte[SIZE/8];
		s.nextBytes(seed);
		String str = "";
		for(byte i : seed){
			System.out.println("Caracter " + i);
			str = str + String.format("%8s",Integer.toBinaryString((i+256)%256)).replace(' ', '0');
		}
		return str;
	}

	public static void write(String name, String s){
		BufferedWriter bw = null;
		try{
			bw = new BufferedWriter(new FileWriter("data\\"+name));
			bw.write(s);
		}catch(Exception e){
			System.out.println(e);
		}
		finally{
			try {
				if (bw != null)
					bw.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}