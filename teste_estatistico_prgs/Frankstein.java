
import java.util.*;
import java.security.SecureRandom;
import java.nio.ByteBuffer;

public class Frankstein
{
    public static void main(String args[]) throws Exception {
        int n = 1000;
        int l = 1000;
        long seed = 0L;
        for (BitSet bitSet : createSequeces(n, l, seed)) {
            for (int i = 0; i < l; i++) {
                System.out.print(((bitSet.get(i)) ? "0" : "1"));
            }
            // System.out.println();
        }
    }

    public static Set<BitSet> createSequeces(int n, int length, long seed ) {
        // check 2^length < n
        Set<BitSet> set = new HashSet<>();
        SecureRandom rand = new SecureRandom(longToBytes(seed));
        while (set.size() < n) {
            set.add(createRandom(rand, length));
        }
        return set;
    }

    private static BitSet createRandom(SecureRandom rand, int length) {
        BitSet secuence = new BitSet(length);
        for (int i = 0; i < length; i++) {
            secuence.set(i, rand.nextBoolean());
        }
        return secuence;
    }

    public static byte[] longToBytes(long x) {
        ByteBuffer buffer = ByteBuffer.allocate(Long.BYTES);
        buffer.putLong(x);
        return buffer.array();
    }
}

//https://stackoverflow.com/questions/39064694/generate-a-sequence-of-random-1s-and-0s
//https://stackoverflow.com/questions/4485128/how-do-i-convert-long-to-byte-and-back-in-java
