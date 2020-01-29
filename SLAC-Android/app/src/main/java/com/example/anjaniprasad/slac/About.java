package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

import java.util.List;

public class About extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
    }

    public void sen(View view)
    {
//        final Intent intent = new Intent(Intent.ACTION_VIEW)
//                .setType("plain/text")
//                .setData(Uri.parse("prasadatluri1997@gmail.com"))
//                .setClassName("com.google.android.gm", "com.google.android.gm.ComposeActivityGmail")
//                .putExtra(Intent.EXTRA_EMAIL, new String[]{"anjaniprasad.almk2015@vit.ac.in"})
//                .putExtra(Intent.EXTRA_SUBJECT, "Reporting an issue")
//                .putExtra(Intent.EXTRA_TEXT, "Hello I am sending this mail to report this issue.");
//        startActivity(intent);

        Intent emailIntent = new Intent(Intent.ACTION_SEND);
        emailIntent.setType("text/html");
        final PackageManager pm = this.getPackageManager();
        final List<ResolveInfo> matches = pm.queryIntentActivities(emailIntent, 0);
        String className = null;
        for (final ResolveInfo info : matches) {
            if (info.activityInfo.packageName.equals("com.google.android.gm")) {
                className = info.activityInfo.name;

                if(className != null && !className.isEmpty()){
                    break;
                }
            }
        }
        emailIntent.setClassName("com.google.android.gm", className);
        emailIntent.putExtra(Intent.EXTRA_EMAIL, new String[]{"anjaniprasad.almk2015@vit.ac.in"});
                emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Reporting an issue");
                emailIntent.putExtra(Intent.EXTRA_TEXT, "Hello I am sending this mail to report this issue.");
                startActivity(emailIntent);
    }

    @Override
    public void onBackPressed() {

        startActivity(new Intent(getApplicationContext(), MainActivity.class));
        finish();

    }
}
