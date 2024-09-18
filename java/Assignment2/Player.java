import java.util.Random;

public class Player {
    private String name;
    private String position;  // forward, midfielder, defender, reserve
    private int seasonGoals;
    private boolean isStar;
    private int kicks;
    private int goals;
    private int behinds;
    private boolean injured;
    private boolean reported;

    public Player(String name, String position, int seasonGoals) {
        this.name = name;
        this.position = position;
        this.seasonGoals = seasonGoals;
        this.isStar = false;
        this.kicks = 0;
        this.goals = 0;
        this.behinds = 0;
        this.injured = false;
        this.reported = false;
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public String getPosition() {
        return position;
    }

    public int getSeasonGoals() {
        return seasonGoals;
    }

    public void setStar(boolean isStar) {
        this.isStar = isStar;
    }

    public boolean isStar() {
        return isStar;
    }

    public void increaseKicks() {
        kicks++;
    }

    public void increaseGoals() {
        goals++;
    }

    public void increaseBehinds() {
        behinds++;
    }

    public int getKicks() {
        return kicks;
    }

    public int getGoals() {
        return goals;
    }

    public int getBehinds() {
        return behinds;
    }

    public boolean isInjured() {
        return injured;
    }

    public void setInjured(boolean injured) {
        this.injured = injured;
    }

    public boolean isReported() {
        return reported;
    }

    public void setReported(boolean reported) {
        this.reported = reported;
    }
}
