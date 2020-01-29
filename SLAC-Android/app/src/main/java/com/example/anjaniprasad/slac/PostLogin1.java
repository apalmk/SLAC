package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class PostLogin1 extends AppCompatActivity {
String name;
    DatabaseReference drr2;
    String atten,miss,moodd,name1;
    String attendee,missed,mooddy;
    List<StdClass> stdcls;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_post_login1);
        Intent iinn= getIntent();
        Bundle b = iinn.getExtras();
stdcls= new ArrayList<>();
        drr2 = FirebaseDatabase.getInstance().getReference("class");

        if(b!=null)
        {
            name =(String) b.get("name");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
        }

    }

    @Override
    protected void onStart() {
        super.onStart();
        drr2.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                stdcls.clear();
                for (DataSnapshot dataSnapshot1:dataSnapshot.getChildren())
                {
                    StdClass sd1=dataSnapshot1.getValue(StdClass.class);
//                    String usern=t1.getName();
//                    System.out.println("Working");
                    name1 = sd1.getName();
                    moodd= sd1.getMood();
                    miss=sd1.getMiss();
                    atten=sd1.getAtten();
//                    Toast.makeText(PostLogin.this,lctt,LENGTH_LONG).show();
                    if(name.equalsIgnoreCase(name1))
                    {
                     attendee=atten;
                     missed=miss;
                     mooddy=moodd;
//                     break;
                    }
                    stdcls.add(sd1);
                }


            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }

    public void sfl(View view)
    {
        Intent myIntent = new Intent(PostLogin1.this, Sfl.class);
        Bundle extras = new Bundle();
        extras.putString("name",name);
        extras.putString("sfl",missed);
        myIntent.putExtras(extras);
        PostLogin1.this.startActivity(myIntent);

    }

    public void mood2(View view)
    {
        Intent myIntent = new Intent(PostLogin1.this, Moody.class);
        Bundle extras = new Bundle();
        extras.putString("name",name);
        extras.putString("moodd",mooddy);
        myIntent.putExtras(extras);
        PostLogin1.this.startActivity(myIntent);
    }

    public void attend(View view)
    {
        Intent myIntent = new Intent(PostLogin1.this, Attendee.class);
        Bundle extras = new Bundle();
        extras.putString("attend",attendee);
        extras.putString("name",name);
        myIntent.putExtras(extras);
        PostLogin1.this.startActivity(myIntent);
    }

public void logoutt(View view)
{
    Intent myIntent = new Intent(PostLogin1.this, MainActivity.class);
    //This shows the ratio of total no of students that slept to that of the students that didn't sleep in the class
    PostLogin1.this.startActivity(myIntent);
}

}
