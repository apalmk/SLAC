package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;
import android.widget.Toast;

public class Lct extends AppCompatActivity {
    private TextView Textv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lct);
        Textv=(TextView)findViewById(R.id.lct_text);
        Intent iin= getIntent();
        Bundle b = iin.getExtras();

        if(b!=null)
        {
            String j =(String) b.get("low");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            Textv.setText(j);
        }
    }

    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Lct.this, PostLogin.class);

        Lct.this.startActivity(myIntent);
    }
}
